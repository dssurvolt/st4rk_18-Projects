package com.example.taskmanager.config;

import com.example.taskmanager.service.JpaUserDetailsService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
public class SecurityConfig {

    private final JpaUserDetailsService userDetailsService;

    public SecurityConfig(JpaUserDetailsService uds) {
        this.userDetailsService = uds;
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        // BCrypt par défaut ; strength peut être ajusté (work factor)
        return new BCryptPasswordEncoder();
    }

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/", "/register", "/css/**", "/js/**", "/h2-console/**").permitAll()
                .anyRequest().authenticated()
            )
            .formLogin(form -> form
                .loginPage("/login")           // page login custom
                .defaultSuccessUrl("/tasks", true)
                .permitAll()
            )
            .logout(logout -> logout
                .logoutUrl("/logout")
                .logoutSuccessUrl("/login?logout")
                .permitAll()
            )
            // pour pouvoir afficher la console H2 (iframe) en dev
            .csrf(csrf -> csrf.ignoringRequestMatchers("/h2-console/**"))
            .headers(headers -> headers.frameOptions(f -> f.disable()))
            ;

        // on indique à Spring Security d'utiliser notre UserDetailsService et PasswordEncoder automatiquement
        return http.build();
    }
}
