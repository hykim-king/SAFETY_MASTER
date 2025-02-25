package com.pcwk.ehr.earthquake.controller;

import com.pcwk.ehr.cmn.SearchVO;
import com.pcwk.ehr.earthquake.domain.EarthquakeVO;
import com.pcwk.ehr.earthquake.service.EarthquakeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@Controller
@RequestMapping("earthquake")
public class EarthquakeController {

    @Autowired
    private EarthquakeService earthquakeService;

    @GetMapping("view")
    public String viewEarthquake(Model model,
                                 @RequestParam(value = "searchWord", defaultValue = "2025")String searchWord,
                                 @RequestParam(value = "searchDiv", defaultValue = "10") int searchDiv) {

        String viewName = "earthquake/earthquake";

        SearchVO search = new SearchVO();
        search.setSearchWord(searchWord);
        search.setSearchDiv(searchDiv);

        try {
            List<EarthquakeVO> list = earthquakeService.getDisMes(search);
            model.addAttribute("list", list);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        return viewName;
    }


}
