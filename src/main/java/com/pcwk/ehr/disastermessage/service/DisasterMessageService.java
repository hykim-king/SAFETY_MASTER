package com.pcwk.ehr.disastermessage.service;

import com.pcwk.ehr.cmn.SearchVO;
import com.pcwk.ehr.disastermessage.domain.DisasterMessageVO;

import java.util.List;

public interface DisasterMessageService {

    List<DisasterMessageVO> getDisMes(SearchVO searchVO) throws Exception;
    int getTotalCount(SearchVO searchVO) throws Exception;

}
