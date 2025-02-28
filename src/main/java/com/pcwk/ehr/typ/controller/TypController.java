package com.pcwk.ehr.typ.controller;

import com.pcwk.ehr.cmn.SearchVO;
import com.pcwk.ehr.typ.domain.TypVO;
import com.pcwk.ehr.typ.service.TypService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@Controller
@RequestMapping("typ")
public class TypController {

    @Autowired
    TypService typService;


    @GetMapping("view")
    public String showTYP(Model model,
                          @RequestParam(value = "searchDiv", defaultValue = "10") int searchDiv,
                          @RequestParam(value = "searchWord", defaultValue = "2023")String searchWord) {
        String viewName = "typ/typ";

        try {
            SearchVO searchVO = new SearchVO();
            searchVO.setSearchDiv(searchDiv);
            searchVO.setSearchWord(searchWord);

            List<TypVO> typ = typService.getTyp(searchVO);
            model.addAttribute("typ", typ);

        } catch (Exception e) {
            throw new RuntimeException(e);
        }


        return viewName;
    }

}
