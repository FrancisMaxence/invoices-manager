from core.comparedir import compare_folders

# Once at launch
#   if invoice date > 6 month:
#       remove invoice (regex or if [date] > 6 month)

# Loop
# each 30 minutes
compare_folders()
# until computer shutdown
