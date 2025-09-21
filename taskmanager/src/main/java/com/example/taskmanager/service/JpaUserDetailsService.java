package com.example.taskmanager.service;

import com.example.taskmanager.model.AppUser;
import com.example.taskmanager.repository.UserRepository;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.*;
import org.springframework.stereotype.Service;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class JpaUserDetailsService implements UserDetailsService {

    private final UserRepository repo;

    public JpaUserDetailsService(UserRepository repo) {
        this.repo = repo;
    }

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        AppUser appUser = repo.findByUsername(username)
                .orElseThrow(() -> new UsernameNotFoundException("Utilisateur non trouvé"));
        // roles are stored like "USER" or "ADMIN,USER"
        List<SimpleGrantedAuthority> authorities = Arrays.stream(appUser.getRoles().split(","))
                .map(String::trim)
                .map(r -> new SimpleGrantedAuthority("ROLE_" + r))
                .collect(Collectors.toList());
        return new User(appUser.getUsername(), appUser.getPassword(), authorities);
    }
}
