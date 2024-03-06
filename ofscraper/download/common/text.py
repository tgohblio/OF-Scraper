import logging
import traceback

import ofscraper.utils.settings as settings
import ofscraper.utils.text as text


def textDownloader(mediadicts):
    log = logging.getLogger("shared")
    try:
        if not "Text" in settings.get_mediatypes():
            log.info("Skipping Downloading of Text Files")
            return
        log.info("Downloading Text Files")
        data = set(map(lambda x: x.postid, mediadicts))
        text.get_text(data)
    except Exception as E:
        log.debug(f"Issue with text {E}")
        log.debug(f"Issue with text {traceback.format_exc()}")
