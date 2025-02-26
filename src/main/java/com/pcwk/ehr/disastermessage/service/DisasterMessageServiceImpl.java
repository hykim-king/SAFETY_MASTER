package com.pcwk.ehr.disastermessage.service;

import com.pcwk.ehr.cmn.SearchVO;
import com.pcwk.ehr.disastermessage.domain.DisasterMessageVO;
import com.pcwk.ehr.disastermessage.mapper.DisasterMessageMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class DisasterMessageServiceImpl implements DisasterMessageService {

    @Autowired
    DisasterMessageMapper disasterMessageMapper;

    @Override
    public List<DisasterMessageVO> getDisMes(SearchVO searchVO) throws Exception {
        // 페이징 처리
        searchVO.setPaging();
        return disasterMessageMapper.getDisMes(searchVO);
    }

    @Override
    public int getTotalCount(SearchVO searchVO) throws Exception {
        return disasterMessageMapper.getTotalCount(searchVO);
    }

    @Override
    public DisasterMessageVO getDisMesDetail(Long id) throws Exception {
        return disasterMessageMapper.getDisMesDetail(id);
    }
}
