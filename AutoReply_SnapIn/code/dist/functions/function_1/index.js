"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.run = void 0;
const typescript_sdk_1 = require("@devrev/typescript-sdk");
function MessageGenerator(event) {
    return __awaiter(this, void 0, void 0, function* () {
        const devrevPAT = event.context.secrets.service_account_token;
        const API_BASE = event.execution_metadata.devrev_endpoint;
        const devrevSDK = typescript_sdk_1.client.setup({
            endpoint: API_BASE,
            token: devrevPAT,
        });
        const entry = event.payload.timeline_entry_created.entry;
        if (entry.body.includes('Auto-Reply:')) {
            console.log('Skiping the Auto-Reply Messages');
            return;
        }
        const startHour = event.input_data.global_values.input_field_1;
        const endHour = event.input_data.global_values.input_field_2;
        const autoReplyMessage = event.input_data.global_values.input_field_3;
        const start_hour = parseInt(startHour, 10);
        const end_hour = parseInt(endHour, 10);
        const createdDate = new Date(entry.created_date);
        const msgHour = createdDate.getHours();
        console.log(`Current hour is: ${msgHour}, Start hour: ${startHour}, End hour: ${endHour}`);
        console.log(`Parsed start hour: ${start_hour}, Parsed end hour: ${end_hour}`);
        if (msgHour < start_hour || msgHour > end_hour) {
            const bodyComment = 'Auto-Reply: '.concat(autoReplyMessage);
            const body = {
                object: entry.object,
                type: 'timeline_comment',
                body: bodyComment,
            };
            const response = yield devrevSDK.timelineEntriesCreate(body);
            console.info(bodyComment);
            return response;
        }
        else {
            console.info('within office hours');
        }
    });
}
const run = (events) => __awaiter(void 0, void 0, void 0, function* () {
    console.info('events', JSON.stringify(events), '\n\n\n');
    for (let event of events) {
        yield MessageGenerator(event);
    }
});
exports.run = run;
exports.default = exports.run;
