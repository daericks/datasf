import numpy as np
import pandas as pd
import pandas_profiling

df = pd.read_csv('/Users/daviderickson/projects/datasf/data/Assessor_Historical_Secured_Property_Tax_Rolls.csv')

# df.profile_report(style={'full_width':True})

profile = df.profile_report()
profile.to_file(output_file="pandas_profile-output.html")