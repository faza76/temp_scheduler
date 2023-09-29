from instagrapi import Client
import os

class BotIG:
    _cl = None
    _media_info = None

    def __init__(self,ig_username, ig_password):
        self._cl = Client()
        credential_path = "../login_sessions/session_" + ig_username + ".json"

        if os.path.exists(credential_path):
            self._cl.load_settings(credential_path)
            self._cl.login(ig_username, ig_password)
            self._cl.get_timeline_feed()
        else:
            self._cl.login(ig_username, ig_password)
            self._cl.dump_settings(credential_path)

    def test(self):
        return "test suc"
    
    def test2(self):
        user_fol = self._cl.user_followers_gql(6149378377)
        return user_fol
    
    def userInfo(self):
        cl = self._cl
        user_info = cl.user_info_by_username('design.boi_').dict()
        return user_info

    def get_media_info(self, link):
        m_pk = self._cl.media_pk_from_url(link)
        self._m_info = self._cl.media_info(m_pk)
        return self._m_info
    
    def post_photo(self, path):
        cl = self._cl
        cl.photo_upload(path = path, caption = "test")

    def post_video(self, path, capt):
        cl = self._cl
        cl.clip_upload(path = path, caption = capt)

    def download_media(self, m_info) -> dict:
        m_pk = m_info.pk
        m_type = m_info.media_type
        result = {}
        paths = []

        if m_type == 1:
            path = self._cl.photo_download(m_pk, '../media/photo')
            paths.append(path)

        if m_type == 2:
            path = self._cl.video_download(m_pk, '../media/video')
            paths.append(path)

        if m_type == 8:
            temp_path = os.path.join('../media/album',str(m_pk))
            os.mkdir(temp_path)
            for path in self._cl.album_download(m_pk,temp_path):
                paths.append(path)        

        result[m_pk] = paths
        return result



