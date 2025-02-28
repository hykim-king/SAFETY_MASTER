package com.pcwk.ehr.disaster_guide.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("disasterguide")
public class DisasterGuideController {

    @GetMapping("/natural")
    public String viewNatural() {
        String viewName = "disasters_guide/natural_disasters_guide";
        return viewName;
    }

    @GetMapping("/social")
    public String viewSocial(){
        String viewName = "disasters_guide/social_disaster_guide";
        return viewName;
    }

}
