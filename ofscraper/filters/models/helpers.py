
import logging
from ofscraper.utils.logs.helpers import is_trace
import ofscraper.utils.constants as constants
log = logging.getLogger("shared")

def trace_log_user(responseArray,filter):
    if not is_trace():
        return
    chunk_size = constants.getattr("LARGE_TRACE_CHUNK_SIZE")
    for i in range(1, len(responseArray) + 1, chunk_size):
        # Calculate end index considering potential last chunk being smaller
        end_index = min(
            i + chunk_size - 1, len(responseArray)
        )  # Adjust end_index calculation
        chunk = responseArray[i - 1 : end_index]  # Adjust slice to start at i-1
        log.trace(
            f"{filter} {{data}}".format(
                data="\n\n".join(list(map(lambda x: f"userdata: {str(x)}", chunk)))
            )
        )
        # Check if there are more elements remaining after this chunk
        if i + chunk_size > len(responseArray):