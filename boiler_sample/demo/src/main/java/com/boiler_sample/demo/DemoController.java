package com.boiler_sample.demo;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class DemoController {

    @GetMapping("/demo")
    public String demo(@RequestParam(name="name", required=false, defaultValue="World") String name, Model model) {
        model.addAttribute("name", name);
        return "demo"; // 템플릿 이름
    }

    @GetMapping("/submit")
    public String submit(@RequestParam(name="name") String name, Model model) {
        model.addAttribute("name", name);
        return "result"; // 결과 페이지 템플릿 이름
    }
}
