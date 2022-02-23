package com.example.gemini.geminiapi;

import edu.gemini.app.ocs.model.StarSystem;

import java.util.ArrayList;

public class StarSystemModel {
    StarSystem.CONSTELLATIONS[] starSystems = StarSystem.CONSTELLATIONS.values();
    public ArrayList<String> getStarSystems() {
        ArrayList<String> results = new ArrayList<>();

        for(StarSystem.CONSTELLATIONS starSystem : starSystems) {
            results.add(starSystem.toString());
        }

        return results;
    }
}
