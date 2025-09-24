import json
import logging
import azure.functions as func

from azure.identity import DefaultAzureCredential
from azure.mgmt.containerservicefleet import ContainerServiceFleetMgmtClient
from azure.core.exceptions import AzureError

app = func.FunctionApp()

@app.event_grid_trigger(arg_name="azeventgrid")
def HandleFleetGateEvent(azeventgrid: func.EventGridEvent):
    logging.info('Python EventGrid trigger processed an event')
    
    event_data = azeventgrid.get_json()

    try:
        event_data = azeventgrid.get_json()
        logging.info(json.dumps(event_data))

        target_id = event_data["resourceInfo"]["properties"]["target"]["id"]
        parts = target_id.split('/')

        # # Extract the values
        # subscription_id = parts[2]  # subscriptions/{subscription_id}
        # resource_group = parts[4]   # resourceGroups/{resource_group}
        # fleet_name = parts[8]       # fleets/{fleet_name}

        # gate_name_uuid = event_data["resourceInfo"]["name"]

        # Create client and update gate
        # client = ContainerServiceFleetMgmtClient(
        #     credential=DefaultAzureCredential(),
        #     subscription_id="" #subscription_id
        # )

        # response = client.gates.begin_update(
        #     resource_group_name="",#resource_group,
        #     fleet_name="",# fleet_name,
        #     gate_name="", #gate_name_uuid,
        #     properties={"properties": {"state": "Completed"}}
        #).result()
        
        #logging.info(f"Successfully updated gate {gate_name_uuid} to Completed state")
        
    except KeyError as e:
        logging.error(f"Missing required field in event data: {e}")
        # Optionally re-raise if you want the function to fail
        # raise
        
    except IndexError as e:
        logging.error(f"Error parsing target_id - unexpected format: {e}")
        
    except AzureError as e:
        logging.error(f"Azure API error: {e}")
        
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        # Optionally re-raise for critical errors
        # raise