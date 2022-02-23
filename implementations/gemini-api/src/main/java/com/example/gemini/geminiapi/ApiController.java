package com.example.gemini.geminiapi;

import edu.gemini.app.ocs.OCS;
import edu.gemini.app.ocs.model.SciencePlan;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;


@RestController
public class ApiController {
    OCS ocs = new OCS();
    SciencePlanModel sciencePlanModel = new SciencePlanModel();
    StarSystemModel starSystemModel = new StarSystemModel();

    @GetMapping("/scienceplan")
    @ResponseBody
    public String getSciencePlanByNo(@RequestParam(defaultValue = "-1") int planNo) throws JSONException {
        if(planNo==-1) {
            return "Error: The Plan No. is missing.";
        }
        return sciencePlanModel.toJson(ocs.getSciencePlanByNo(planNo));
    }

    @GetMapping("/scienceplans")
    @ResponseBody
    public String getSciencePlans(@RequestParam(defaultValue = "") String status,
                                  @RequestParam(defaultValue = "") String creator) throws JSONException {
        ArrayList<SciencePlan> sciencePlans = ocs.getAllSciencePlans();

        if(!status.equals("")) {
            sciencePlans = sciencePlanModel.getSciencePlansByStatus(sciencePlans, status);
        }

        if(!creator.equals("")) {
            sciencePlans = sciencePlanModel.getSciencePlansByCreator(sciencePlans, creator);
        }

        System.out.println("{\"sciencePlans\":" + sciencePlanModel.toJson(sciencePlans).toString() + "}");

        return "{\"sciencePlans\":" + sciencePlanModel.toJson(sciencePlans).toString() + "}";
    }

    @PostMapping(
            value = "/scienceplan",
            consumes = {MediaType.APPLICATION_FORM_URLENCODED_VALUE})
    public String createSciencePlan(TransferClass transferObject) throws Exception {
        SciencePlan sp = transferObject.toSciencePlan();
        ocs.submitSciencePlan(sp);

        JSONObject response = new JSONObject();
        response.put("planNo", sp.getPlanNo());

        System.out.println(response);

        return response.toString();
    }

    @GetMapping("/starsystems")
    @ResponseBody
    public String getStarSystems() throws JSONException {
        ArrayList<String> starSystems = starSystemModel.getStarSystems();

        JSONObject jsonStarSystems = new JSONObject();
        jsonStarSystems.put("starSystems", new JSONArray(starSystems));

        return jsonStarSystems.toString();
    }

    @GetMapping("/telescopelocations")
    @ResponseBody
    public String getTelescopeLocations() throws JSONException {
        ArrayList<String> telescopeLocations = new ArrayList<>();
        telescopeLocations.add("HAWAII");
        telescopeLocations.add("CHILE");

        JSONObject jsonTelescopeLocations = new JSONObject();
        jsonTelescopeLocations.put("telescopeLocations", new JSONArray(telescopeLocations));

        return jsonTelescopeLocations.toString();
    }

    @PostMapping(
            value = "/test",
            consumes = {MediaType.APPLICATION_FORM_URLENCODED_VALUE})
    public String testSciencePlan(TransferClass transferObject) throws Exception {
        SciencePlan sp = transferObject.updateSciencePlan();

        JSONObject response = new JSONObject();
        response.put("testResult", ocs.testSciencePlan(sp));
        response.put("status", ocs.getSciencePlanByNo(sp.getPlanNo()).getStatus().toString());

        System.out.println(response);

        return response.toString();
    }

    @PostMapping(
            value = "/validate",
            consumes = {MediaType.APPLICATION_FORM_URLENCODED_VALUE})
    public void validateSciencePlan(int planNo, String status) {
        ocs.updateSciencePlanStatus(planNo, SciencePlan.STATUS.valueOf(status));
        System.out.println(ocs.getAllSciencePlans());
    }
}