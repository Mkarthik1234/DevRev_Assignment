import { client } from "@devrev/typescript-sdk";

async function MessageGenerator(
  event: any,
) {
  const devrevPAT = event.context.secrets.service_account_token;
  const API_BASE = event.execution_metadata.devrev_endpoint;

  
  const devrevSDK = client.setup({
    endpoint: API_BASE,
    token: devrevPAT,
  });

  const entry = event.payload.timeline_entry_created.entry; //taking the entry values from the event payload

  //in order to avoid generating reply for auto reply time line entries
  if (entry.body.includes('Auto-Reply:')) {
    console.log('Skiping the Auto-Reply Messages');
    return;
  }
  
  //taking values given in input fields of snap in configuration
  const startHour = event.input_data.global_values.input_field_1;
  const endHour = event.input_data.global_values.input_field_2;
  const autoReplyMessage = event.input_data.global_values.input_field_3;

  //converting text to inteager
  const start_hour = parseInt(startHour,10);
  const end_hour = parseInt(endHour,10);

  //taking the created date from the entry to get the message created hour
  const createdDate = new Date(entry.created_date);
  const msgHour = createdDate.getHours();


  console.log(`Current hour is: ${msgHour}, Start hour: ${startHour}, End hour: ${endHour}`);
  console.log(`Parsed start hour: ${start_hour}, Parsed end hour: ${end_hour}`);

  //checking for message out of office hours
  if (msgHour < start_hour || msgHour > end_hour) {

    const bodyComment = 'Auto-Reply: '.concat(autoReplyMessage);

    const body = {
      object: entry.object,
      type: 'timeline_comment',
      body: bodyComment,
    };

    const response = await devrevSDK.timelineEntriesCreate(body as any);//creating timeline entry
    console.info(bodyComment);

    return response;
  
  } else {
    // if message is within office hours
    console.info('within office hours');
  }
}

export const run = async (events: any[]) => {
  console.info('events', JSON.stringify(events), '\n\n\n');
  for (let event of events) {
    await MessageGenerator(event); //calling Auto reply function
  }
};

export default run;
