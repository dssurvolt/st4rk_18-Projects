
package com.example.taskmanager.repository;

import com.example.taskmanager.model.Task;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface TaskRepository extends JpaRepository<Task, Long> {
    List<Task> findByUserUsername(String username);
    // On peut ajouter des méthodes spécifiques si besoin, par ex. :
    // List<Task> findByCompleted(boolean completed);
}
