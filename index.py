from core.comparedir import compare_folders

# Loop
# each 30 minutes
compare_folders()

#   if invoice date > 6 month:
#       remove invoice (regex or if [date] > 6 month)
# until computer shutdown