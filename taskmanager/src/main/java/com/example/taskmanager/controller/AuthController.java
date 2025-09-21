package com.example.taskmanager.controller;

import com.example.taskmanager.service.UserService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class AuthController {

    private final UserService userService;

    public AuthController(UserService userService) { this.userService = userService; }

    @GetMapping("/register")
    public String showRegister(Model model) {
        return "register";
    }

    @PostMapping("/register")
    public String doRegister(@RequestParam String username,
                             @RequestParam String password,
                             @RequestParam(required = false) String email,
                             Model model) {
        try {
            userService.registerUser(username, password, email);
            return "redirect:/login?registered";
        } catch (IllegalArgumentException ex) {
            model.addAttribute("error", ex.getMessage());
            return "register";
        }
    }

    @GetMapping("/login")
    public String loginPage() {
        return "login";
    }
}
