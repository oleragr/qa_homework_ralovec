from api.base_API import BaseAPI
import json


class ToggleUserStatusAPI(BaseAPI):

    def __init__(self):
        BaseAPI.__init__(self)

    def toggle_user_status(self, account_nr, msisdn, is_admin):
        payload = json.dumps({"isAdmin": is_admin})
        resp = self.session.post(self.base_url + f"{account_nr}/{msisdn}/admin", data=payload)
        return resp
