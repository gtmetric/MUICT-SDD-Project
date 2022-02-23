package com.example.gemini.geminiapi;

import edu.gemini.app.ocs.OCS;
import edu.gemini.app.ocs.model.DataProcRequirement;
import edu.gemini.app.ocs.model.SciencePlan;
import edu.gemini.app.ocs.model.StarSystem;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class SciencePlanModel {
    OCS ocs = new OCS();

     public ArrayList<SciencePlan> getSciencePlansByCreator(String creator) {
         return getSciencePlansByCreator(ocs.getAllSciencePlans(), creator);
    }

    public ArrayList<SciencePlan> getSciencePlansByCreator(ArrayList<SciencePlan> sciencePlans, String creator) {
        ArrayList<SciencePlan> result = new ArrayList<>();

        for (SciencePlan sp : sciencePlans) {
            String c = sp.getCreator();
            if(creator.equals(c)) {
                result.add(sp);
            }
        }

        return result;
    }

    public ArrayList<SciencePlan> getSciencePlansByStatus(String status) {
        return getSciencePlansByStatus(ocs.getAllSciencePlans(), status);
    }

    public ArrayList<SciencePlan> getSciencePlansByStatus(ArrayList<SciencePlan> sciencePlans, String status) {
         ArrayList<SciencePlan> result = new ArrayList<>();
        SciencePlan.STATUS statusEnum = SciencePlan.STATUS.valueOf(status);

        for (SciencePlan sp : sciencePlans) {
            SciencePlan.STATUS s = sp.getStatus();
            if(statusEnum.equals(s)) {
                result.add(sp);
            }
        }

        return result;
    }

    public ArrayList<SciencePlan> getAllSciencePlansBySubmitter(String submitter) {
        ArrayList<SciencePlan> sciencePlans = ocs.getAllSciencePlans();

        for (SciencePlan sp : sciencePlans) {
            String s = sp.getCreator();
            if(!submitter.equals(s)) {
                sciencePlans.remove(sp);
            }
        }

        return sciencePlans;
    }

    public String toJson(SciencePlan sciencePlan) throws JSONException {
         int planNo = sciencePlan.getPlanNo();
         String creator = sciencePlan.getCreator();
         String submitter = sciencePlan.getSubmitter();
         double funding = sciencePlan.getFundingInUSD();
         String objectives = sciencePlan.getObjectives();
         StarSystem.CONSTELLATIONS starSystem = sciencePlan.getStarSystem();
         String startDate = sciencePlan.getStartDate();
         String endDate = sciencePlan.getEndDate();
         SciencePlan.TELESCOPELOC location = sciencePlan.getTelescopeLocation();
         DataProcRequirement req = sciencePlan.getDataProcRequirements();
         SciencePlan.STATUS status = sciencePlan.getStatus();

         JSONObject reqJson = new JSONObject();
         reqJson.put("fileType", req.getFileType());
         reqJson.put("colorType", req.getColorType());
         reqJson.put("contrast", req.getContrast());
         reqJson.put("brightness", req.getBrightness());
         reqJson.put("saturation", req.getSaturation());
         reqJson.put("hightlight", req.getHighlights());
         reqJson.put("exposure", req.getExposure());
         reqJson.put("shadows", req.getShadows());
         reqJson.put("whites", req.getWhites());
         reqJson.put("blacks", req.getBlacks());
         reqJson.put("luminance", req.getLuminance());
         reqJson.put("hue", req.getHue());

         JSONObject jsonObject = new JSONObject();
         jsonObject.put("planNo", planNo);
         jsonObject.put("creator", creator);
         jsonObject.put("submitter", submitter);
         jsonObject.put("funding", funding);
         jsonObject.put("objectives", objectives);
         jsonObject.put("starSystem", starSystem);
         jsonObject.put("startDate", startDate);
         jsonObject.put("endDate", endDate);
         jsonObject.put("location", location);
         jsonObject.put("requirments", reqJson);
         jsonObject.put("status", status);

         return jsonObject.toString();
    }

    public ArrayList<String> toJson(ArrayList<SciencePlan> sciencePlans) throws JSONException {
         ArrayList<String> result = new ArrayList<String>();

        for (SciencePlan sp : sciencePlans) {
            result.add(toJson(sp));
        }

        return result;
    }
}
