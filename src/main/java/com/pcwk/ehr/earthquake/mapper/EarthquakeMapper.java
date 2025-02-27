package com.pcwk.ehr.earthquake.mapper;

import com.pcwk.ehr.cmn.SearchVO;
import com.pcwk.ehr.disastermessage.domain.DisasterMessageVO;
import com.pcwk.ehr.earthquake.domain.EarthquakeVO;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface EarthquakeMapper {

    List<EarthquakeVO> getEQK (SearchVO searchVO);
    List<EarthquakeVO> eqkByYear ();
    List<EarthquakeVO> eqkOccurrence (SearchVO searchVO);
}
