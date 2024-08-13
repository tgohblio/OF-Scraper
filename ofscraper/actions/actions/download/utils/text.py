import logging
import traceback

import ofscraper.classes.media as media_class
import ofscraper.actions.utils.log as logs
import ofscraper.utils.settings as settings
import ofscraper.utils.text as text
from ofscraper.utils.context.run_async import run
import ofscraper.utils.args.accessors.read as read_args


@run
async def textDownloader(objectdicts, username=None):
    log = logging.getLogger("shared")
    if read_args.retriveArgs().command == "metadata":
        return
    if not bool(objectdicts):
        return
    try:
        if not settings.get_download_text():
            log.info("Skipping Downloading of Text Files")
            return
        objectdicts = (
            [objectdicts] if not isinstance(objectdicts, list) else objectdicts
        )
        log.info("Downloading Text Files")
        data = (
            {
                e.postid if isinstance(e, media_class.Media) else e.id: e
                for e in objectdicts
            }
        ).values()
        count, fails, exists = await text.get_text(data)
        username = username or "Unknown"
        logs.text_log(username, count, fails, exists, log=log)
    except Exception as E:
        log.debug(f"Issue with text {E}")
        log.debug(f"Issue with text {traceback.format_exc()}")
