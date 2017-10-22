package Model.model;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

/**
 * Created by mastercljohnson on 10/21/2017.
 */

public class Match {
    @SerializedName("confidence")
    @Expose
    private Double confidence;
    @SerializedName("face_uid")
    @Expose
    private String faceUid;
    @SerializedName("is_match")
    @Expose
    private Boolean isMatch;
    @SerializedName("person_name")
    @Expose
    private String personName;

    public Double getConfidence() {
        return confidence;
    }

    public void setConfidence(Double confidence) {
        this.confidence = confidence;
    }

    public String getFaceUid() {
        return faceUid;
    }

    public void setFaceUid(String faceUid) {
        this.faceUid = faceUid;
    }

    public Boolean getIsMatch() {
        return isMatch;
    }

    public void setIsMatch(Boolean isMatch) {
        this.isMatch = isMatch;
    }

    public String getPersonName() {
        return personName;
    }

    public void setPersonName(String personName) {
        this.personName = personName;
    }
}
