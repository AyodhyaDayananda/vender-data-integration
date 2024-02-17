import azure.functions as func
import logging
from zoom import main
from asb_handler import service_provider

app = func.FunctionApp()

# @app.queue_trigger(arg_name="azqueue", queue_name="zoom-vender",
#                                connection="e1d891_STORAGE") 
# def zoom_vender_queue_trigger(azqueue: func.QueueMessage):
#     logging.info('Python Queue trigger processed a message: %s',
#                 azqueue.get_body().decode('utf-8'))



@app.service_bus_topic_trigger(arg_name="azservicebus", subscription_name="zoom_servicebus_topic_trigger", topic_name="zoom_servicebus_topic_trigger",
                               connection="ayodemo_SERVICEBUS") 
def zoom_servicebus_topic_trigger(azservicebus: func.ServiceBusMessage):
    params = azservicebus.get_body().decode('utf-8')
    asb_handler = service_provider.ServiceProvide()
    asb_handler.get_params(params=params)
    logging.info('Python ServiceBus Topic trigger processed a message: %s',
                azservicebus.get_body().decode('utf-8'))
