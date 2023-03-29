import json
import logging
import azure.functions as func


def main(event: func.EventHubEvent):
    decodedBodyEvent = event.get_body().decode()
    logging.info(f'Function triggered to process a message: {decodedBodyEvent}')
    logging.info(f'EnqueuedTimeUtc = {event.enqueued_time}')
    logging.info(f'SequenceNumber = {event.sequence_number}')
    logging.info(f'Offset = {event.offset}')

    result = json.dumps(decodedBodyEvent)


    logging.info(f'Python EventGrid trigger processed an event: {result}')



