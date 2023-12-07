import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class LogTask {

    private static final Logger logger = LogManager.getLogger(LogTask.class);

    public static void main(String[] args) {
        // Logique à exécuter
        logger.info("Ceci est un message de log depuis LogTask.");
    }
}
