import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.Timer;
import java.util.TimerTask;

public class PeriodicLogging {

    private static final Logger logger = LogManager.getLogger(PeriodicLogging.class);

    public static void main(String[] args) {
        Timer timer = new Timer(true);

        // Planifie une tâche périodique toutes les 5 secondes (5000 millisecondes)
        timer.scheduleAtFixedRate(new LogTask(), 0, 5000);
    }

    static class LogTask extends TimerTask {
        @Override
        public void run() {
            // Logique à exécuter périodiquement
            logger.info("Ceci est un message de log périodique.");
        }
    }
}
