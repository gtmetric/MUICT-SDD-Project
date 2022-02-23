import edu.gemini.app.ocs.OCS;
import edu.gemini.app.ocs.example.MySciencePlan;
import edu.gemini.app.ocs.model.AstronomicalData;
import edu.gemini.app.ocs.model.DataProcRequirement;
import edu.gemini.app.ocs.model.SciencePlan;
import edu.gemini.app.ocs.model.StarSystem;

import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        OCS ocs = new OCS(true);

        ocs.updateSciencePlanStatus(1, SciencePlan.STATUS.VALIDATED);
        ocs.updateSciencePlanStatus(2, SciencePlan.STATUS.INVALIDATED);
    }
}
