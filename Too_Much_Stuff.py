import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import gspread

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(credentials)

MenteesId = '1shFQ5KtOxGZ9IJdCcFVo9FtAGtpnoJ7GYYfc7x8SaVs'
MentorsId = '1PGNGMNS5vg3Lt4xGIuSmHBXgKgTQQlIPF8rJXUbBnuQ'
OutputId = '14m89nbA7ST_fLA5S20piFXRUwvSO-YJqbBcViLzt8E4'

def read_rawMentees():
  sheet = 'Answers'
  return (pd.read_csv(f"https://docs.google.com/spreadsheets/d/{MenteesId}/gviz/tq?tqx=out:csv&sheet={sheet}"))

def read_rawMentors():
  sheet = 'Answers'
  return (pd.read_csv(f"https://docs.google.com/spreadsheets/d/{MentorsId}/gviz/tq?tqx=out:csv&sheet={sheet}"))











