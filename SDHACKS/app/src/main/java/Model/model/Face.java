package Model.model;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.List;

/**
 * Created by mastercljohnson on 10/21/2017.
 */

public class Face {
    @SerializedName("angle")
    @Expose
    private Double angle;
    @SerializedName("height")
    @Expose
    private Double height;
    @SerializedName("image_uid")
    @Expose
    private String imageUid;
    @SerializedName("person_name")
    @Expose
    private String personName;
    @SerializedName("points")
    @Expose
    private List<Point> points = null;
    @SerializedName("score")
    @Expose
    private Double score;
    @SerializedName("tags")
    @Expose
    private List<Tag> tags = null;
    @SerializedName("uid")
    @Expose
    private String uid;
    @SerializedName("user_points")
    @Expose
    private List<UserPoint> userPoints = null;
    @SerializedName("width")
    @Expose
    private Double width;
    @SerializedName("x")
    @Expose
    private Double x;
    @SerializedName("y")
    @Expose
    private Double y;

    public Double getAngle() {
        return angle;
    }

    public void setAngle(Double angle) {
        this.angle = angle;
    }

    public Double getHeight() {
        return height;
    }

    public void setHeight(Double height) {
        this.height = height;
    }

    public String getImageUid() {
        return imageUid;
    }

    public void setImageUid(String imageUid) {
        this.imageUid = imageUid;
    }

    public String getPersonName() {
        return personName;
    }

    public void setPersonName(String personName) {
        this.personName = personName;
    }

    public List<Point> getPoints() {
        return points;
    }

    public void setPoints(List<Point> points) {
        this.points = points;
    }

    public Double getScore() {
        return score;
    }

    public void setScore(Double score) {
        this.score = score;
    }

    public List<Tag> getTags() {
        return tags;
    }

    public void setTags(List<Tag> tags) {
        this.tags = tags;
    }

    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public List<UserPoint> getUserPoints() {
        return userPoints;
    }

    public void setUserPoints(List<UserPoint> userPoints) {
        this.userPoints = userPoints;
    }

    public Double getWidth() {
        return width;
    }

    public void setWidth(Double width) {
        this.width = width;
    }

    public Double getX() {
        return x;
    }

    public void setX(Double x) {
        this.x = x;
    }

    public Double getY() {
        return y;
    }

    public void setY(Double y) {
        this.y = y;
    }

}
