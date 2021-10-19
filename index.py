from core.comparedir import compare_directories

# Loop
# each 30 minutes
compare_directories()

#   if invoice date > 6 month:
#       remove invoice (regex or if [date] > 6 month)
# until computer shutdown