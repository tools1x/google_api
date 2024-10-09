import gspread

OAUTH = {"installed": {"client_id": "1081276071884-epc7id9dmmb3eteteshig7oef9idtgdr.apps.googleusercontent.com",
                       "project_id": "rpazenno-405917", "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                       "token_uri": "https://oauth2.googleapis.com/token",
                       "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                       "client_secret": "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", "redirect_uris": ["http://localhost"]}}
AUTH_USER = {
  "refresh_token" : "1//09ge45HgFSYGrCgYIARAAGAkSNwF-L9Ir-xGX-9_eSnkX"
                    "O7JSRdCFQ9M8s_vBJ39QCUO-v4eYtLhlymeAyw5-FXb5gK3eRb8NsTM",
  "token_uri" : "https://oauth2.googleapis.com/token",
  "client_id" : "1081276071884-epc7id9dmmb3eteteshig7oef9idtgdr.apps.googleusercontent.com",
  "client_secret" : "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",
  "scopes" : [ "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive" ],
  "universe_domain" : "googleapis.com",
  "account" : "alex_rpa@1xpartner.com",
}

def get_client():
    return gspread.oauth_from_dict(credentials=OAUTH, authorized_user_info=AUTH_USER)[0]
