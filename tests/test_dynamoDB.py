class DynamoDBClient:
  def __init__(self, table_name, region_name):
    # Crear cliente de DynamoDB
    self.dynamodb_client = boto3.resource('dynamodb', region_name=region_name)
    self.table = self.dynamodb_client.Table(table_name)

  def crear_item(self, item):
    # Almacenar un elemento en la tabla de DynamoDB
    self.table.put_item(Item=item)

  def leer_item(self, item_id):
    # Leer un elemento de la tabla de DynamoDB
    response = self.table.get_item(Key={'id': item_id})
    return response.get('Item')

  def actualizar_item(self, item_id, item_updates):
    # Actualizar un elemento en la tabla de DynamoDB
    self.table.update_item(Key={'id': item_id}, UpdateExpression="SET {}".format(item_updates))

  def eliminar_item(self, item_id):
    # Eliminar un elemento de la tabla de DynamoDB
    self.table.delete_item(Key={'id': item_id})