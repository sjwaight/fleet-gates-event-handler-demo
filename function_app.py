import json
import logging
import azure.functions as func

from types import SimpleNamespace
from azure.identity import DefaultAzureCredential
from azure.mgmt.containerservicefleet import ContainerServiceFleetMgmtClient

app = func.FunctionApp()

@app.event_grid_trigger(arg_name="azeventgrid")
def HandleFleetGateEvent(azeventgrid: func.EventGridEvent):
    logging.info('Python EventGrid trigger processed an event')

    # event = json.loads(json.dumps(azeventgrid.get_json()), object_hook=lambda d: SimpleNamespace(**d))

    # target_id = event.data.resourceInfo.properties.target.id
    # parts = target_id.split('/')

    # # Extract the values
    # subscription_id = parts[2]  # subscriptions/{subscription_id}
    # resource_group = parts[4]   # resourceGroups/{resource_group}
    # fleet_name = parts[8]       # fleets/{fleet_name}

    # data = azeventgrid.get_json()

    # # read the name value for the gate
    # gate_name_uuid = data["resourceInfo"]["name"]

    # # perform other functions
    # # ....
    # # ....

    # client = ContainerServiceFleetMgmtClient(
    #   credential=DefaultAzureCredential(),
    #   subscription_id=subscription_id,
    # )

    # response = client.gates.begin_update(
    #   resource_group_name=resource_group,
    #   fleet_name=fleet_name,
    #   gate_name=gate_name_uuid,
    #   properties={"properties": {"state": "Completed"}},
    # ).result()