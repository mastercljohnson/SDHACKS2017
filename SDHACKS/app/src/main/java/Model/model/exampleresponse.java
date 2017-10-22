package Model.model;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.List;

/**
 * Created by mastercljohnson on 10/21/2017.
 */

public class exampleresponse {
    @SerializedName("int_response")
    @Expose
    private Integer intResponse;
    @SerializedName("string_response")
    @Expose
    private String stringResponse;
    @SerializedName("checksum")
    @Expose
    private String checksum;
    @SerializedName("faces")
    @Expose
    private List<Face> faces = null;
    @SerializedName("faces_matches")
    @Expose
    private List<FacesMatch> facesMatches = null;
    @SerializedName("original_filename")
    @Expose
    private String originalFilename;
    @SerializedName("uid")
    @Expose
    private String uid;

    public Integer getIntResponse() {
        return intResponse;
    }

    public void setIntResponse(Integer intResponse) {
        this.intResponse = intResponse;
    }

    public String getStringResponse() {
        return stringResponse;
    }

    public void setStringResponse(String stringResponse) {
        this.stringResponse = stringResponse;
    }

    public String getChecksum() {
        return checksum;
    }

    public void setChecksum(String checksum) {
        this.checksum = checksum;
    }

    public List<Face> getFaces() {
        return faces;
    }

    public void setFaces(List<Face> faces) {
        this.faces = faces;
    }

    public List<FacesMatch> getFacesMatches() {
        return facesMatches;
    }

    public void setFacesMatches(List<FacesMatch> facesMatches) {
        this.facesMatches = facesMatches;
    }

    public String getOriginalFilename() {
        return originalFilename;
    }

    public void setOriginalFilename(String originalFilename) {
        this.originalFilename = originalFilename;
    }

    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }


}
