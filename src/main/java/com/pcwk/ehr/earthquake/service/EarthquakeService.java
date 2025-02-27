package com.pcwk.ehr.earthquake.service;

import com.pcwk.ehr.cmn.EQK_DTO;
import com.pcwk.ehr.cmn.SearchVO;
import com.pcwk.ehr.earthquake.domain.EarthquakeVO;


import java.util.List;

public interface EarthquakeService {

    List<EarthquakeVO> getDisMes(SearchVO searchVO) throws Exception;
    List<EQK_DTO> eqkByYear ();
}
