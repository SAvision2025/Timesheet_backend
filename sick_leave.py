# import pymongo
# import datetime

# def accrue_sick_leave_for_employee(employee_name):
#     client = pymongo.MongoClient("mongodb+srv://prashitar:Vision123@cluster0.v7ckx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#     db = client["Timesheet"]
#     emp_data_collection = db["employee_data"]
#     employee_pm_collection = db["Employee_PM"]
#     employee_leave_collection = db["Employee_leavedetails"]

#     today = datetime.datetime.now().date()

#     employee = emp_data_collection.find_one({"name": employee_name})
#     if not employee:
#         return (f"Employee {employee_name} not found in employee_data.")
#         return

#     print(f"\nProcessing employee: {employee_name}")

#     leave_data = employee_leave_collection.find_one({"name": employee_name})
#     if not leave_data:
#         return(f"No leave data found for {employee_name}. Skipping.")
#         return

#     last_accrued_date_str = leave_data.get("last_accrued_date")
#     carried_over = leave_data.get("Carried_over_hours", 0)
#     current_earned_hours = leave_data.get("Earned_hours", 0)
#     sick_leave = leave_data.get("Sick_leave_hours", 0)
#     total_leave = leave_data.get("Total_leave_hours", 0)
#     remaining_leave = leave_data.get("Remaining_leave_hours", 0)

#     if last_accrued_date_str:
#         last_accrued_date = datetime.datetime.strptime(last_accrued_date_str, "%Y-%m-%d").date()
#     else:
#         last_accrued_date = today

#     if today.month == 1 and today.day == 1 and today.year > last_accrued_date.year:
#         employee_leave_collection.update_one(
#             {"name": employee_name},
#             {"$set": {
#                 "Earned_hours": 0,
#                 "Carried_over_hours": 0,
#                 "Casual_leave_hours": 40,
#                 "last_accrued_date": today.strftime("%Y-%m-%d")
#             }}
#         )
#         print(f"{employee_name}'s Earned and Carried hours reset for the new year.")
#         return

#     query = {"employee_name": employee_name, "date": {"$gt": last_accrued_date.strftime("%Y-%m-%d")}}
#     total_new_hours = 0
#     for record in employee_pm_collection.find(query):
#         hours_list = record.get("hours", [])
#         total_new_hours += len(hours_list)

#     total_hours = total_new_hours + carried_over
#     print(total_new_hours)
#     earned_sick_leave = total_hours // 30
#     remaining_carry = total_hours % 30  

#     print(f"{employee_name} worked {total_new_hours} hours -> {earned_sick_leave} sick leave hours earned")

#     actual_earned_hours = min(earned_sick_leave, max(0, 72 - current_earned_hours))
#     if actual_earned_hours == 0:
#         print(f"Max earned sick leave reached for {employee_name}. No hours added.")

#     if actual_earned_hours > 0:
#         new_sick_leave = sick_leave + actual_earned_hours
#         new_total_leave = total_leave + actual_earned_hours
#         new_remaining_leave = remaining_leave + actual_earned_hours
#         new_earned_hours = current_earned_hours + actual_earned_hours

#         update_result = employee_leave_collection.update_one(
#             {"name": employee_name},
#             {"$set": {
#                 "Earned_hours": new_earned_hours,
#                 "Carried_over_hours": remaining_carry,
#                 "Sick_leave_hours": new_sick_leave,
#                 "Total_leave_hours": new_total_leave,
#                 "Remaining_leave_hours": new_remaining_leave,
#                 "last_accrued_date": today.strftime("%Y-%m-%d")
#             }}
#         )

#         print(f"Updated {employee_name}: {update_result.modified_count} document(s)")



##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################



# import pymongo
# import datetime

# def accrue_sick_leave_for_employee(employee_name):
# #     client = pymongo.MongoClient("mongodb+srv://prashitar:Vision123@cluster0.v7ckx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#     client = pymongo.MongoClient("mongodb+srv://timesheetsystem:SinghAutomation2025@cluster0.alcdn.mongodb.net/")
#     db = client["Timesheet"]
#     emp_data_collection = db["Employee_data"]
#     employee_pm_collection = db["Employee_PM"]
#     employee_leave_collection = db["Employee_leavedetails"]

#     today = datetime.datetime.now().date()

#     employee = emp_data_collection.find_one({"name": employee_name})
#     if not employee:
#         return f"Employee {employee_name} not found in employee_data."

#     leave_data = employee_leave_collection.find_one({"name": employee_name})
#     if not leave_data:
#         return f"No leave data found for {employee_name}. Skipping."

#     last_accrued_date_str = leave_data.get("last_accrued_date")
#     carried_over = leave_data.get("Carried_over_hours", 0)
#     current_earned_hours = leave_data.get("Earned_hours", 0)
#     sick_leave = leave_data.get("Sick_leave_hours", 0)
#     total_leave = leave_data.get("Total_leave_hours", 0)
#     remaining_leave = leave_data.get("Remaining_leave_hours", 0)

#     if last_accrued_date_str:
#         last_accrued_date = datetime.datetime.strptime(last_accrued_date_str, "%Y-%m-%d").date()
#     else:
#         last_accrued_date = today

#     if today.month == 1 and today.day == 1 and today.year > last_accrued_date.year:
#         employee_leave_collection.update_one(
#             {"name": employee_name},
#             {"$set": {
#                 "Earned_hours": 0,
#                 "Carried_over_hours": 0,
#                 "Casual_leave_hours": 40,
#                 "last_accrued_date": today.strftime("%Y-%m-%d")
#             }}
#         )
#         return f"{employee_name}'s Earned and Carried hours reset for the new year."

#     query = {"employee_name": employee_name, "date": {"$gt": last_accrued_date.strftime("%Y-%m-%d")}}
#     total_new_hours = 0
#     for record in employee_pm_collection.find(query):
#         hours_list = record.get("hours", [])
#         total_new_hours += len(hours_list)

#     total_hours = total_new_hours + carried_over
#     earned_sick_leave = total_hours // 30
#     remaining_carry = total_hours % 30  

#     actual_earned_hours = min(earned_sick_leave, max(0, 72 - current_earned_hours))
#     if actual_earned_hours == 0:
#         return f"{employee_name} worked {total_new_hours} hours. Max earned sick leave reached. No hours added."
#     # if actual_earned_hours == 0:
#     #     employee_leave_collection.update_one(
#     #         {"name": employee_name},
#     #         {"$set": {
#     #             "Carried_over_hours": remaining_carry,
#     #             "last_accrued_date": today.strftime("%Y-%m-%d")
#     #         }}
#     #     )
#     #     return f"{employee_name} worked {total_new_hours} hours. Max earned sick leave reached. No hours added."

#     new_sick_leave = sick_leave + actual_earned_hours
#     new_total_leave = total_leave + actual_earned_hours
#     new_remaining_leave = remaining_leave + actual_earned_hours
#     new_earned_hours = current_earned_hours + actual_earned_hours

#     update_result = employee_leave_collection.update_one(
#         {"name": employee_name},
#         {"$set": {
#             "Earned_hours": new_earned_hours,
#             "Carried_over_hours": remaining_carry,
#             "Sick_leave_hours": new_sick_leave,
#             "Total_leave_hours": new_total_leave,
#             "Remaining_leave_hours": new_remaining_leave,
#             "last_accrued_date": today.strftime("%Y-%m-%d")
#         }}
#     )

#     return (
#         f"{employee_name} worked {total_new_hours} hours -> "
#         f"{actual_earned_hours} sick leave hours earned. "
#         f"Updated {update_result.modified_count} document(s)."
#     )




import pymongo
import datetime
import logging

# Setup logging — logs will appear in Render dashboard under "Logs"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def accrue_sick_leave_for_employee(employee_name):
    client = pymongo.MongoClient("mongodb+srv://timesheetsystem:SinghAutomation2025@cluster0.alcdn.mongodb.net/")
    db = client["Timesheet"]
    emp_data_collection = db["Employee_data"]
    employee_pm_collection = db["Employee_PM"]
    employee_leave_collection = db["Employee_leavedetails"]

    today = datetime.datetime.now().date()

    employee = emp_data_collection.find_one({"name": employee_name})
    if not employee:
        logging.error(f"Employee '{employee_name}' not found in employee_data.")
        return

    leave_data = employee_leave_collection.find_one({"name": employee_name})
    if not leave_data:
        logging.warning(f"No leave data found for '{employee_name}'. Skipping accrual.")
        return

    last_accrued_date_str = leave_data.get("last_accrued_date")
    carried_over = leave_data.get("Carried_over_hours", 0)
    current_earned_hours = leave_data.get("Earned_hours", 0)
    sick_leave = leave_data.get("Sick_leave_hours", 0)
    total_leave = leave_data.get("Total_leave_hours", 0)
    remaining_leave = leave_data.get("Remaining_leave_hours", 0)

    if last_accrued_date_str:
        last_accrued_date = datetime.datetime.strptime(last_accrued_date_str, "%Y-%m-%d").date()
    else:
        last_accrued_date = today

    # Reset on Jan 1
    if today.month == 1 and today.day == 1 and today.year > last_accrued_date.year:
        employee_leave_collection.update_one(
            {"name": employee_name},
            {"$set": {
                "Earned_hours": 0,
                "Carried_over_hours": 0,
                "Casual_leave_hours": 40,
                "last_accrued_date": today.strftime("%Y-%m-%d")
            }}
        )
        logging.info(f"{employee_name}'s leave data reset for the new year.")
        return

    # Calculate hours worked since last accrual
    query = {"employee_name": employee_name, "date": {"$gt": last_accrued_date.strftime("%Y-%m-%d")}}
    total_new_hours = sum(len(record.get("hours", [])) for record in employee_pm_collection.find(query))
    total_hours = total_new_hours + carried_over
    earned_sick_leave = total_hours // 30
    remaining_carry = total_hours % 30

    # Cap at 72 hours max
    actual_earned_hours = min(earned_sick_leave, max(0, 72 - current_earned_hours))
    if actual_earned_hours == 0:
        logging.info(
            f"{employee_name} worked {total_new_hours} hours. Max sick leave cap reached (72 hrs). "
            f"No new hours added."
        )
        return
    # if actual_earned_hours == 0:
    #     employee_leave_collection.update_one(
    #         {"name": employee_name},
    #         {"$set": {
    #             "Carried_over_hours": remaining_carry,
    #             "last_accrued_date": today.strftime("%Y-%m-%d")
    #         }}
    #     )
    #     return f"{employee_name} worked {total_new_hours} hours. Max earned sick leave reached. No hours added."


    # Update leave fields
    new_sick_leave = sick_leave + actual_earned_hours
    new_total_leave = total_leave + actual_earned_hours
    new_remaining_leave = remaining_leave + actual_earned_hours
    new_earned_hours = current_earned_hours + actual_earned_hours

    result = employee_leave_collection.update_one(
        {"name": employee_name},
        {"$set": {
            "Earned_hours": new_earned_hours,
            "Carried_over_hours": remaining_carry,
            "Sick_leave_hours": new_sick_leave,
            "Total_leave_hours": new_total_leave,
            "Remaining_leave_hours": new_remaining_leave,
            "last_accrued_date": today.strftime("%Y-%m-%d")
        }}
    )

    logging.info(
        f"{employee_name}: {total_new_hours} hrs worked -> {actual_earned_hours} hrs sick leave earned. "
        f"Document updated: {result.modified_count}."
    )
