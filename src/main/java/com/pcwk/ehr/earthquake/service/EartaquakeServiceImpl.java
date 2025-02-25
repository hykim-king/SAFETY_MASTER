package com.pcwk.ehr.earthquake.service;

import com.pcwk.ehr.cmn.SearchVO;
import com.pcwk.ehr.earthquake.domain.EarthquakeVO;
import com.pcwk.ehr.earthquake.mapper.EarthquakeMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class EartaquakeServiceImpl implements EarthquakeService {

    @Autowired
    EarthquakeMapper earthquakeMapper;

    @Override
    public List<EarthquakeVO> getDisMes(SearchVO searchVO) throws Exception {
        return earthquakeMapper.getEQK(searchVO);
    }
}
