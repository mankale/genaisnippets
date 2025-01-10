# This code snippet is to use UpdateIndex API for Amazon Q Business. This example shows how document attributes can be configured for an index.

import boto3
import json
from botocore.exceptions import ClientError

def update_index(index_id, description=None, documentAttributeConfigurations=None):
    """
    Update an Amazon Q Business index
    
    Parameters:
    - index_id (str): The ID of the index to update
    - name (str): New name for the index (optional)
    - description (str): New description for the index (optional)
    """
    try:
        # Create Amazon Q Business client
        q_client = boto3.client('qbusiness')
        
        # Prepare update parameters
        update_params = {
            'id': index_id
        }

        # Add optional parameters if provided
        #if name:
        #    update_params['name'] = name
        if description:
            update_params['description'] = description

        # Call UpdateIndex API
        response = q_client.update_index(**{
            'indexId': index_id,
            'applicationId': "<enter your application-id>",  # You will get application id in AWS Console
            'description': description,
            'documentAttributeConfigurations': documentAttributeConfigurations
        })
        
        print(f"Successfully updated index: {index_id}")
        return response
        
    except ClientError as e:
        print(f"Error updating index: {e.response['Error']['Message']}")
        raise
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise

def main():
    # Replace these values with your actual index details
    INDEX_ID = '<enter your index-id>' # You will get index id in AWS Console
    NEW_DESCRIPTION = 'Amazon Q Business HR Assistant'  # Optional
    documentAttributeConfigurations = [ 
      { 
         "name": "_view_count",
         "search": "ENABLED",
         "type": "NUMBER"
      }, 
      { 
         "name": "_data_source_id",
         "search": "ENABLED",
         "type": "STRING"
      },
      {
         "name": "_last_updated_at",
         "type": "DATE",
         "search": "ENABLED"
      }
   ]

    
    try:
        # Get AWS credentials from environment variables
        session = boto3.Session()
        
        # Update the index
        result = update_index(
            index_id=INDEX_ID,
            #name=NEW_NAME,
            description=NEW_DESCRIPTION,
            documentAttributeConfigurations=documentAttributeConfigurations
        )
        
        # Print the response
        print(json.dumps(result, indent=2, default=str))
        
    except Exception as e:
        print(f"Error in main: {str(e)}")

if __name__ == '__main__':
    main()
