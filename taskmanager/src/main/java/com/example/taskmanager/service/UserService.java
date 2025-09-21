package com.example.taskmanager.service;

import com.example.taskmanager.model.AppUser;
import com.example.taskmanager.repository.UserRepository;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    public UserService(UserRepository repo, PasswordEncoder encoder) {
        this.userRepository = repo;
        this.passwordEncoder = encoder;
    }

    public AppUser registerUser(String username, String rawPassword, String email) {
        if (userRepository.existsByUsername(username)) {
            throw new IllegalArgumentException("Nom d'utilisateur déjà pris");
        }
        if (email != null && userRepository.existsByEmail(email)) {
            throw new IllegalArgumentException("Email déjà utilisé");
        }
        String encoded = passwordEncoder.encode(rawPassword);
        AppUser user = new AppUser(username, encoded, "USER", email);
        return userRepository.save(user);
    }

    public AppUser findByUsername(String username) {
        return userRepository.findByUsername(username).orElse(null);
    }
}
