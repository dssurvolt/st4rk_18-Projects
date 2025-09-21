
package com.example.taskmanager;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.boot.CommandLineRunner;
import com.example.taskmanager.service.UserService;

@SpringBootApplication
public class TaskmanagerApplication {

    @Bean
    public CommandLineRunner initUsers(UserService userService) {
        return args -> {
            if (userService.findByUsername("admin") == null) {
                userService.registerUser("admin", "password", "admin@example.com");
                // si tu veux un rôle ADMIN, il faut modifier userService pour permettre la création avec roles "ADMIN,USER"
            }
        };
    }

    public static void main(String[] args) {
        SpringApplication.run(TaskmanagerApplication.class, args);
    }

}
