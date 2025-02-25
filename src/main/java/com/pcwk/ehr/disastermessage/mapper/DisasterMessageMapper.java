package com.pcwk.ehr.disastermessage.mapper;

import com.pcwk.ehr.cmn.SearchVO;
import com.pcwk.ehr.disastermessage.domain.DisasterMessageVO;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface DisasterMessageMapper {

    List<DisasterMessageVO> getDisMes(SearchVO searchVO);
    int getTotalCount(SearchVO searchVO);
    int doRetrieveWhere();
}
