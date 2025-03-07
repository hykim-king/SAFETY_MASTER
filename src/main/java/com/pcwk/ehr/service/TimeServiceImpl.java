package com.pcwk.ehr.service;

import com.pcwk.ehr.mapper.TimeMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class TimeServiceImpl implements TimeService {

    @Autowired
    TimeMapper timeMapper;

    final Logger log = LoggerFactory.getLogger(getClass());

    @Override
    public String getNewDateTime() {
        return timeMapper.getNewDateTime();
    }

    @Override
    public String getDateTime() {
        return timeMapper.getDateTime();
    }
}
