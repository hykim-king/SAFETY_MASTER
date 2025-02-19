package com.pcwk.ehr.controller;

import com.pcwk.ehr.service.TimeService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class TimeController {

    final Logger log = LoggerFactory.getLogger(getClass());

    @Autowired
    TimeService timeService;

    public TimeController() {
        log.info("TimeController");
    }

    @GetMapping("/getNewDateTime.do")
    @ResponseBody
    public String getNewDateTime() {
        log.info("getNewDateTime");

        String dateTime= timeService.getNewDateTime();

        log.info("getNewDateTime: "+dateTime);

        return dateTime;
    }

}
