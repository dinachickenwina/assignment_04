"""
payroll_app.py — the weekly payroll, for someone who has never opened a terminal.

Every Friday the office manager at Salt City Coffee exports the week's timesheet
from the point-of-sale system. This page turns it into a paycheck table and the
CSV the online payroll provider imports — without the manager touching pandas.

The app is mostly *assembly*: the roster is loaded from data/, the upload comes
from the page, and one call to `build_payroll` does all the work. What the page
adds is what a manager needs to trust the numbers: totals, a loud warning about
anything the pipeline could not match, the full lineage table, and the download.

Run it:  Run and Debug -> "Streamlit Run: Current File"   (see README Reference #1)
Test it: pytest tests/test_pipeline.py -k app
"""

# --- The page ---------------------------------------------------------------------
#
# No scaffolding. Every function this page needs already exists in the payroll
# package, and every widget it needs you used in Assignment 03. README Step 8 has
# the exact widgets, keys and labels; the tests in tests/test_pipeline.py -k app
# check them.
#
# The shape, in words:
#
#   title and a sentence of instructions
#   roster  <- load_employees()                      (fixed; not uploaded)
#   upload  <- st.file_uploader, key="timesheet"     (returns None until chosen)
#   if there is an upload:
#       timesheet <- load_timesheet(upload)
#       payroll   <- build_payroll(timesheet, roster)   one call does all the work
#       the pay period (payroll_date) as a subheader
#       four st.metric cards in st.columns(4) — totals are .sum() on a Series,
#           counts are len() of a boolean-indexed frame
#       st.warning naming the unmatched employee_ids, or st.success if none
#       st.dataframe(payroll) — the lineage table, raw and computed side by side
#       st.download_button, key="download": payroll_export(payroll).to_csv(index=False)
#
# What the page does NOT do: arithmetic on rows, cleaning, merging. If you find
# yourself writing a loop or an apply here, that logic belongs in the package.

import streamlit as st

from payroll import build_payroll, load_employees, load_timesheet, payroll_export

st.title("Salt City Coffee — Weekly Payroll")
st.write("Upload this week's timesheet to review payroll and download the provider file.")

employees = load_employees()
uploaded_timesheet = st.file_uploader("Upload timesheet CSV", type="csv", key="timesheet")

if uploaded_timesheet is not None:
	timesheet = load_timesheet(uploaded_timesheet)
	payroll = build_payroll(timesheet, employees)
	payroll_date = payroll["payroll_date"].iloc[0]

	st.subheader(str(payroll_date))
	metrics = st.columns(4)
	metrics[0].metric("Employees paid", len(payroll[payroll["pay_type"] != "unmatched"]))
	metrics[1].metric("Total hours", f"{payroll['hours_worked'].sum():.2f}")
	metrics[2].metric("Total gross pay", f"${payroll['gross_pay'].sum():,.2f}")
	metrics[3].metric("Overtime weeks", len(payroll[payroll["pay_type"] == "overtime"]))

	unmatched_ids = payroll.loc[payroll["pay_type"] == "unmatched", "employee_id"].tolist()
	if unmatched_ids:
		st.warning(f"Unmatched employee IDs: {', '.join(map(str, unmatched_ids))}")
	else:
		st.success("All employee IDs matched the roster.")

	st.dataframe(payroll)
	csv_data = payroll_export(payroll).to_csv(index=False)
	st.download_button(
		"Download payroll CSV",
		data=csv_data,
		file_name=f"payroll_{payroll_date}.csv",
		mime="text/csv",
		key="download",
	)
