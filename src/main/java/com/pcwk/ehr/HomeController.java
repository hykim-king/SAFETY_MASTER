package com.pcwk.ehr;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {
	
	@GetMapping("/home")
	public String home() {
		
		System.out.println("home sweet home !!");
		
		return "home";
	} 

}
