# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         sfp_local_data
# Purpose:      Spiderfoot plugin to check if data occurs in a local leak or breach dataset.
# -------------------------------------------------------------------------------

import json

from spiderfoot import SpiderFootEvent, SpiderFootPlugin


class sfp_local_data(SpiderFootPlugin):

    meta = {
        'name': "Local data",
        'summary': "Check whether data is found in a breach or leak dataset",
        'flags': ["slow"],
        'useCases': ["Investigate", "Passive"],
        'categories': ["Leaks, Dumps and Breaches"],
    }

    opts = {
        "local_path_list": [""],
        "use_mail": True,
        "use_phone": True
    }

    optdescs = {
        "local_path_list": "A comma seperated list of full filepaths of the datasets you want to use.",
        "use_mail": "if the module should listen for emails",
        "use_phone": "if the module should listen for phone numbers"
    }

    results = None
    errorState = False

    def setup(self, sfc, userOpts=dict()):
        self.sf = sfc
        self.results = self.tempStorage()

        for opt in list(userOpts.keys()):
            self.opts[opt] = userOpts[opt]

    def watchedEvents(self):
        watchedEventList = []
        if self.opts["use_mail"]:
            watchedEventList.append("EMAILADDR")
        if self.opts["use_phone"]:
            watchedEventList.append('PHONE_NUMBER')

        return watchedEventList

    def producedEvents(self):
        return [
            "RAW_RIR_DATA"
        ]

    def queryEmailAddr(self, qry):
        lines = {}
        for dataset in self.opts["local_path_list"]:
            with open(dataset, 'r') as inF:
                linecount = 0
                for line in inF:
                    linecount = linecount + 1
                    if qry in line:
                        lines[dataset + " line: " + str(linecount)] = line

        if lines == {}:
            self.info(f"No local data info found for {qry}")
            return None

        res = json.dumps(lines)
        try:
            return json.loads(res)
        except Exception as e:
            self.error(f"Error processing datasets: {e}")

        return None

    # Handle events sent to this module
    def handleEvent(self, event):
        eventName = event.eventType
        srcModuleName = event.module
        eventData = event.data

        if self.errorState:
            return

        self.debug(f"Received event, {eventName}, from {srcModuleName}")

        self.results[eventData] = True

        data = self.queryEmailAddr(eventData)

        if data is None:
            return


        evt = SpiderFootEvent("RAW_RIR_DATA", str(data), self.__name__, event)
        self.notifyListeners(evt)

# End of sfp_local_data class
