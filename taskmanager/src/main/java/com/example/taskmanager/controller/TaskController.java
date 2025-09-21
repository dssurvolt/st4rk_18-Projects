package com.example.taskmanager.controller;

import com.example.taskmanager.model.AppUser;
import com.example.taskmanager.model.Task;
import com.example.taskmanager.service.UserService;
import com.example.taskmanager.repository.TaskRepository;
import com.example.taskmanager.repository.UserRepository;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import java.security.Principal;
import jakarta.validation.Valid;
import org.springframework.validation.BindingResult;

@Controller
@RequestMapping("/tasks")
public class TaskController {

    private final TaskRepository taskRepository;
    private final UserService userService;

    public TaskController(TaskRepository taskRepository, UserService userService) {
        this.taskRepository = taskRepository;
        this.userService = userService;
    }

    @GetMapping
    public String listTasks(Model model, Principal principal) {
        String username = principal.getName();
        model.addAttribute("tasks", taskRepository.findByUserUsername(username));
        model.addAttribute("task", new Task());
        model.addAttribute("username", username);
        return "tasks";
    }

    @PostMapping
    public String addTask(@Valid @ModelAttribute Task task, BindingResult result, Principal principal, Model model) {
        if (result.hasErrors()) {
            model.addAttribute("tasks", taskRepository.findByUserUsername(principal.getName()));
            return "tasks";
        }
        AppUser user = userService.findByUsername(principal.getName());
        task.setUser(user);
        taskRepository.save(task);
        return "redirect:/tasks";
    }

    @PostMapping("/delete/{id}")
    public String deleteTask(@PathVariable Long id, Principal principal) {
        Task t = taskRepository.findById(id).orElse(null);
        if (t == null) return "redirect:/tasks";
        if (!t.getUser().getUsername().equals(principal.getName())) {
            return "redirect:/access-denied"; // ou lancer exception
        }
        taskRepository.deleteById(id);
        return "redirect:/tasks";
    }

    @PostMapping("/toggle/{id}")
    public String toggleCompleted(@PathVariable Long id, Principal principal) {
        Task t = taskRepository.findById(id).orElse(null);
        if (t == null) return "redirect:/tasks";
        if (!t.getUser().getUsername().equals(principal.getName())) {
            return "redirect:/access-denied";
        }
        t.setCompleted(!t.isCompleted());
        taskRepository.save(t);
        return "redirect:/tasks";
    }
}
