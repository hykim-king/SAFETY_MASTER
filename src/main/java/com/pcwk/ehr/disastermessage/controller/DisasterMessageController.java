package com.pcwk.ehr.disastermessage.controller;

import com.pcwk.ehr.cmn.SearchVO;
import com.pcwk.ehr.disastermessage.domain.DisasterMessageVO;
import com.pcwk.ehr.disastermessage.service.DisasterMessageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@Controller
@RequestMapping("disastermessage")
public class DisasterMessageController {

    @Autowired
    DisasterMessageService disasterMessageService;

    @GetMapping("view")
    public String showDisasterMessage(@RequestParam(value = "pageNo", defaultValue = "1") int pageNo,
                                      @RequestParam(value = "pageSize", defaultValue = "10") int pageSize,
                                      @RequestParam(value = "searchDiv", defaultValue = "") String searchDiv,
                                      @RequestParam(value = "searchWord", defaultValue = "") String searchWord,
                                      Model model) {

        String viewName = "disastermessage/disastermessage";

        try {
            SearchVO searchVO = new SearchVO();
            searchVO.setPageNo(pageNo);
            searchVO.setPageSize(pageSize);
            searchVO.setSearchDiv(searchDiv);
            searchVO.setSearchWord(searchWord);
            searchVO.setPaging();

            List<DisasterMessageVO> list = disasterMessageService.getDisMes(searchVO);
            model.addAttribute("list", list);
            model.addAttribute("searchDiv", searchDiv);
            model.addAttribute("searchWord", searchWord);

            // 총 글 수 조회하여 페이지네이션 계산
            int totalCnt = disasterMessageService.getTotalCount(searchVO);
            model.addAttribute("totalCnt", totalCnt);
            model.addAttribute("totalPage", (int) Math.ceil((double) totalCnt / pageSize));

        } catch (Exception e) {
            e.printStackTrace();
        }

        return viewName;
    }

}
