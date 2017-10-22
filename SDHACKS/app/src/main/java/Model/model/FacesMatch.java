package Model.model;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.List;

/**
 * Created by mastercljohnson on 10/21/2017.
 */

public class FacesMatch {
    @SerializedName("face_uid")
    @Expose
    private String faceUid;
    @SerializedName("matches")
    @Expose
    private List<Match> matches = null;

    public String getFaceUid() {
        return faceUid;
    }

    public void setFaceUid(String faceUid) {
        this.faceUid = faceUid;
    }

    public List<Match> getMatches() {
        return matches;
    }

    public void setMatches(List<Match> matches) {
        this.matches = matches;
    }
}
